#!/usr/bin/env node

import fs from 'node:fs';
import path from 'node:path';
import process from 'node:process';

const repoRoot = process.cwd();
const registryPath = path.join(repoRoot, 'data', 'controlled-terms.json');

function readJson(filePath) {
  try {
    return JSON.parse(fs.readFileSync(filePath, 'utf8'));
  } catch (error) {
    console.error(`[controlled-terms] Unable to read JSON: ${filePath}`);
    console.error(error.message);
    process.exit(2);
  }
}

function normalizePath(value) {
  return value.split(path.sep).join('/');
}

function walkDirectory(dir, options, files = []) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    const relativePath = normalizePath(path.relative(repoRoot, fullPath));

    if (entry.isDirectory()) {
      if (options.ignoredDirectories.includes(entry.name) || options.ignoredDirectories.includes(relativePath)) {
        continue;
      }
      walkDirectory(fullPath, options, files);
      continue;
    }

    if (!entry.isFile()) {
      continue;
    }

    const extension = path.extname(entry.name);
    if (options.textExtensions.includes(extension)) {
      files.push({ fullPath, relativePath });
    }
  }
  return files;
}

function countOccurrences(haystack, needle) {
  if (!needle) return 0;
  let count = 0;
  let index = 0;
  while ((index = haystack.indexOf(needle, index)) !== -1) {
    count += 1;
    index += needle.length;
  }
  return count;
}

function main() {
  const registry = readJson(registryPath);
  const auditPolicy = registry.audit_policy || {};
  const options = {
    ignoredDirectories: auditPolicy.ignored_directories || ['.git', 'node_modules'],
    textExtensions: auditPolicy.text_extensions || ['.html', '.md', '.json', '.js', '.mjs', '.css', '.svg', '.yml', '.yaml']
  };

  const files = walkDirectory(repoRoot, options);
  const failures = [];
  const warnings = [];

  for (const termSet of registry.controlled_term_sets || []) {
    const allowedReferenceFiles = new Set(termSet.allowed_reference_files || []);
    const requiredTermFiles = termSet.required_term_files || [];
    const forbiddenTerms = termSet.forbidden_terms || [];
    const canonicalTerm = termSet.canonical_term;

    for (const file of files) {
      const content = fs.readFileSync(file.fullPath, 'utf8');
      const isAllowedReference = allowedReferenceFiles.has(file.relativePath);

      for (const forbiddenTerm of forbiddenTerms) {
        const occurrences = countOccurrences(content, forbiddenTerm);
        if (occurrences > 0 && !isAllowedReference) {
          failures.push({
            type: 'forbidden_term',
            termSet: termSet.id,
            file: file.relativePath,
            term: forbiddenTerm,
            occurrences
          });
        }
      }
    }

    if (canonicalTerm && requiredTermFiles.length > 0) {
      for (const requiredFile of requiredTermFiles) {
        const fullPath = path.join(repoRoot, requiredFile);
        if (!fs.existsSync(fullPath)) {
          warnings.push({
            type: 'missing_required_file',
            termSet: termSet.id,
            file: requiredFile
          });
          continue;
        }
        const content = fs.readFileSync(fullPath, 'utf8');
        if (!content.includes(canonicalTerm)) {
          failures.push({
            type: 'missing_canonical_term',
            termSet: termSet.id,
            file: requiredFile,
            term: canonicalTerm,
            occurrences: 0
          });
        }
      }
    }
  }

  if (warnings.length > 0) {
    console.warn('[controlled-terms] Warnings:');
    for (const warning of warnings) {
      console.warn(`- ${warning.type}: ${warning.termSet} -> ${warning.file}`);
    }
  }

  if (failures.length > 0) {
    console.error('[controlled-terms] Drift detected.');
    for (const failure of failures) {
      console.error(`- ${failure.type}: ${failure.termSet} -> ${failure.file} -> "${failure.term}" (${failure.occurrences})`);
    }
    process.exit(1);
  }

  console.log('[controlled-terms] PASS: no controlled-term drift detected.');
}

main();
