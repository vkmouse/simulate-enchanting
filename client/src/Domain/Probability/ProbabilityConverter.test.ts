import ProbabilityConverter from "./ProbabilityConverter";

test('expand zero range', () => {
  const convertor = new ProbabilityConverter();
  const probs = convertor.expandRange(0, 0, 1);
  expect(probs.length).toBe(1);
  expect(probs[0]).toBe(0);
});

test('expand single range', () => {
  const convertor = new ProbabilityConverter();
  const probs = convertor.expandRange(0, 1, 1);
  expect(probs.length).toBe(2);
  expect(probs[0]).toBe(0);
  expect(probs[1]).toBe(1);
});

test('expand continuous range', () => {
  const convertor = new ProbabilityConverter();
  const probs = convertor.expandRange(0, 4, 1);
  expect(probs.length).toBe(5);
  expect(probs[0]).toBe(0);
  expect(probs[1]).toBe(1);
  expect(probs[2]).toBe(2);
  expect(probs[3]).toBe(3);
  expect(probs[4]).toBe(4);
});

test('expand discrete range', () => {
  const convertor = new ProbabilityConverter();
  const probs = convertor.expandRange(0, 4, 2);
  expect(probs.length).toBe(3);
  expect(probs[0]).toBe(0);
  expect(probs[1]).toBe(2);
  expect(probs[2]).toBe(4);
});
