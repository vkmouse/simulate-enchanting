import RouletteSimulator from "./RouletteSimulator";

test('spin', () => {
  const rouletteSimulator = new RouletteSimulator();
  expect(rouletteSimulator.spin([0.5, 0.5], () => 0.3)).toBe(0);
  expect(rouletteSimulator.spin([0.5, 0.5], () => 0.5)).toBe(1);
  expect(rouletteSimulator.spin([0.5, 0.5], () => 1.0)).toBe(1);
  expect(rouletteSimulator.spin([0.3, 1.0], () => 0.3)).toBe(1);
});
