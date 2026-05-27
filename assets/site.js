const serviceSubjects = {
  ride: 'Private Ride Request',
  matchday: 'Matchday Inquiry',
  airport: 'Airport Transfer Request',
  hospitality: 'Concierge Hospitality Request',
  group: 'Group and VIP Transportation Request',
  luggage: 'Luggage Coordination Request'
};

function buildMailto(subject, body) {
  const email = 'concierge@dfwmatchdayconcierge.com';
  return `mailto:${email}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
}

function setServiceFromQuery(form) {
  const params = new URLSearchParams(window.location.search);
  const service = params.get('service');
  if (!service) return;
  const select = form.querySelector('select[name="service"]');
  if (select && serviceSubjects[service]) select.value = service;
}

function wireInquiryForm() {
  const form = document.querySelector('[data-inquiry-form]');
  if (!form) return;
  setServiceFromQuery(form);
  form.addEventListener('submit', event => {
    event.preventDefault();
    const data = new FormData(form);
    const service = data.get('service') || 'General Inquiry';
    const subject = serviceSubjects[service] || 'DFW Matchday Concierge Inquiry';
    const body = [
      'DFW Matchday Concierge Inquiry',
      '',
      `Name: ${data.get('name') || ''}`,
      `Phone: ${data.get('phone') || ''}`,
      `Email: ${data.get('email') || ''}`,
      `Service: ${form.querySelector(`[value="${service}"]`)?.textContent || service}`,
      `Pickup / Location: ${data.get('location') || ''}`,
      `Date / Time: ${data.get('datetime') || ''}`,
      '',
      'Details:',
      data.get('details') || ''
    ].join('\n');
    window.location.href = buildMailto(subject, body);
  });
}

document.addEventListener('DOMContentLoaded', wireInquiryForm);
