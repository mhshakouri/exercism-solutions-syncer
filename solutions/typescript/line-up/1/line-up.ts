const numberSuffix = (number: number): string => {
  switch (number % 10) {
    case 1:
      return number % 100 !== 11 ? 'st' : 'th'
    case 2:
      return number % 100 !== 12 ? 'nd' : 'th'
    case 3:
      return number % 100 !== 13 ? 'rd' : 'th'
    default:
      return 'th'
  }
}

const formatterNumber = (number: number): string => {
  const numberToString = number.toString()
  return `${numberToString}${numberSuffix(number)}`
}

export function format(name: string, number: number): string {
  return `${name}, you are the ${formatterNumber(number)} customer we serve today. Thank you!`
}
