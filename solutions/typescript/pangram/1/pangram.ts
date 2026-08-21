export function isPangram(sentence: string): boolean {
  const alphabet = 'abcdefghijklmnopqrstuvwxyz';
  const sentenceLower = sentence.toLowerCase();
  for (const letter of alphabet) {
    if (!sentenceLower.includes(letter)) {
      return false;
    }
  }
  return true;
}
