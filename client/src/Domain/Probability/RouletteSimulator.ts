class RouletteSimulator {
  private random = () => {
    return Math.random();
  };

  spin(probs: Array<number>, random=this.random): number {
    const rnd = random();
    probs = this.createRoulette(probs);
    for (let i = 1; i < probs.length; i++) {
      if (probs[i - 1] <= rnd && rnd < probs[i]) {
        return i - 1;
      }
    }
    return probs.length - 2;
  }

  private createRoulette(probs: Array<number>) {
    const sum = probs.reduce((prev, curr) => prev + curr, 0);
    probs = [0].concat(probs);
    for (let i = 1; i < probs.length; i++) {
      probs[i] = probs[i] / sum + probs[i - 1];
    }
    probs[probs.length - 1] = 1.000001;
    return probs;
  }
}
  
  export default RouletteSimulator;