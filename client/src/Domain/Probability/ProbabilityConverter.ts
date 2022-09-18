class ProbabilityConverter {
  expandRange(start: number, stop: number, step: number): Array<number> {
    const values = [];
    for (let i = start; i < stop + 1; i = i + step) {
        values.push(i);
    }
    return values;
  }
}

export default ProbabilityConverter;