# DFW GitHub Execution Governance and Branch Policy v1.0.0

## 1. Controlled Action

This file satisfies audit correction R-005 by defining the GitHub execution policy for future DFW Matchday Concierge corrections, skeleton work, production work, and deployment-related changes.

This file records that the current correction package was user-authorized as an urgent correction mission and executed directly on `main`. Future high-risk execution must use branch and PR workflow unless the user explicitly authorizes a direct-to-main exception.

## 2. Status

Status: ACTIVE GITHUB EXECUTION POLICY

Activation standing:

`BRANCH POLICY CREATED / FUTURE HIGH-RISK EXECUTION DEFAULTS TO BRANCH AND PR / DIRECT-TO-MAIN REQUIRES EXPLICIT USER AUTHORIZATION`

## 3. Default Governance Rule

The default path for future correction, skeleton, homepage, production, deployment, QR, CI, and public route changes is:

1. Create a branch from `main`.
2. Commit bounded changes to the branch.
3. Open a pull request to `main`.
4. Review changed files.
5. Verify allowed paths and blocked paths.
6. Run CI when available or complete manual verification.
7. Merge only after user approval where required.

## 4. Direct-to-Main Exception Rule

Direct-to-main commits may occur only when all conditions are true:

1. The user explicitly authorizes execution.
2. The mission is bounded.
3. The file targets are known.
4. The action does not deploy, activate QR, or approve production.
5. Post-commit fetch verification is performed.
6. Commit SHAs are returned.
7. Activation status remains accurately reported.

## 5. Current Correction Mission Exception Record

Mission:

`dfw_ai_governed_premium_website_builder_audit_corrections_blocker_clearance_package`

Execution standing:

Direct-to-main correction execution was user-authorized in this workspace for correction files only.

Boundary:

1. No skeleton files.
2. No homepage files.
3. No public route edits.
4. No DreamHost deployment.
5. No QR activation.
6. No production approval.
7. No self-clearance of activation.

## 6. Required Verification After Direct-to-Main Commit

Every direct-to-main correction must return:

1. File path.
2. Commit SHA.
3. Exact fetch verification from `main`.
4. Activation impact.
5. Remaining blockers or user evaluation requirements.

## 7. High-Risk File Categories

Branch and PR workflow is required by default for:

1. `index.html`.
2. `connect/index.html`.
3. `contact/index.html`.
4. `services/index.html`.
5. Service route files.
6. `sitemap.xml`.
7. `robots.txt`.
8. Production deployment files.
9. QR assets.
10. GitHub workflow files.
11. Future skeleton prototype files.
12. Any final content-bearing page.

## 8. Final Determination

Audit correction R-005 is satisfied.

Final standing:

`GITHUB EXECUTION GOVERNANCE CREATED / FUTURE HIGH-RISK WORK DEFAULTS TO BRANCH AND PR / DIRECT-TO-MAIN REQUIRES EXPLICIT USER AUTHORIZATION AND POST-COMMIT VERIFICATION`.
