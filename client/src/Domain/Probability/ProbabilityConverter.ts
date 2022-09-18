class ProbabilityConverter {
  convertRange(start: number, stop: number, step: number): Array<number> {
    const probs = [];
    for (let i = start; i < stop + 1; i = i + step) {
        probs.push(i);
    }
    return probs;
  }
}

export default ProbabilityConverter;