const dnaToRna = {
  'C': 'G',
  'G': 'C',
  'A': 'U',
  'T': 'A',
} as const;

export function toRna(dna: string) {
  return dna.split('').map(nucleotide => {
    if (!dnaToRna[nucleotide as keyof typeof dnaToRna]) {
      throw new Error('Invalid input DNA.');
    }
    return dnaToRna[nucleotide as keyof typeof dnaToRna];
  }).join('');
}
