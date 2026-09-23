import test from 'node:test';
import assert from 'node:assert/strict';
import { buildParticipantsList } from '../src/static/activity-card.mjs';

test('buildParticipantsList renders a participant bullet list', () => {
  const html = buildParticipantsList(['alice@mergington.edu', 'bob@mergington.edu']);

  assert.match(html, /Participants/);
  assert.match(html, /<ul class="participants-list">/);
  assert.match(html, /alice@mergington.edu/);
  assert.match(html, /bob@mergington.edu/);
});

test('buildParticipantsList shows an empty state when no one has signed up yet', () => {
  const html = buildParticipantsList([]);

  assert.match(html, /No participants yet/);
  assert.match(html, /participants-empty/);
});
