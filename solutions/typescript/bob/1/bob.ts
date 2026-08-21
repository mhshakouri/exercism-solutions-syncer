const isSilence = (message: string): boolean => message.trim().length === 0;
const isYelling = (message: string): boolean =>
  /[A-Za-z]/.test(message) && message.trim().toUpperCase() === message.trim();
const isQuestion = (message: string): boolean => message.trim().endsWith('?');

export function hey(message: string): string {
  if (isSilence(message)) {
    return 'Fine. Be that way!';
  } else {
    if (isQuestion(message) && isYelling(message)) {
      return 'Calm down, I know what I\'m doing!';
    } else if (isQuestion(message) && !isYelling(message)) {
      return 'Sure.';
    } else if (isYelling(message)) {
      return 'Whoa, chill out!';
    } else {
      return 'Whatever.';
    }
  }
}
