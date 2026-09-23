export function buildParticipantsList(participants = [], activityName = "") {
  if (!participants || participants.length === 0) {
    return `
      <p class="participants-empty">No participants yet. Be the first to sign up!</p>
    `;
  }

  const items = participants
    .map(
      (participant) => `
        <li class="participant-item">
          <span class="participant-email">${participant}</span>
          <button
            type="button"
            class="participant-remove"
            data-activity-name="${activityName}"
            data-email="${participant}"
            aria-label="Remove ${participant} from ${activityName}"
            title="Remove ${participant}"
          >
            <span aria-hidden="true">✕</span>
          </button>
        </li>
      `
    )
    .join("");

  return `
    <ul class="participants-list">
      ${items}
    </ul>
  `;
}
