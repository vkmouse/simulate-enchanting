import EnchantedAttributeCalculater from "./EnchantedAttributeCalculater";

test('sum attributes', () => {
  const calculater = new EnchantedAttributeCalculater();
  const attributeRows = [{
    value: 3,
    name: 'First Attribute',
    isPercentage: true,
    rowNumber: 1,
  }, {
    value: 3,
    name: 'First Attribute',
    isPercentage: true,
    rowNumber: 2,
  }, {
    value: 3,
    name: 'Second Attribute',
    isPercentage: true,
    rowNumber: 3,
  }];
  const attributes = calculater.sum(attributeRows);
  expect(attributes.length).toBe(2);
  expect(attributes[0]).toStrictEqual({
    value: 6,
    name: 'First Attribute',
    isPercentage: true
  });
  expect(attributes[1]).toStrictEqual({
    value: 3,
    name: 'Second Attribute',
    isPercentage: true
  });
});

test('sum attributes with different isPercentage', () => {
  const calculater = new EnchantedAttributeCalculater();
  const attributeRows = [{
    value: 3,
    name: 'First Attribute',
    isPercentage: true,
    rowNumber: 1,
  }, {
    value: 3,
    name: 'First Attribute',
    isPercentage: false,
    rowNumber: 2,
  }];
  const attributes = calculater.sum(attributeRows);
  expect(attributes.length).toBe(2);
  expect(attributes[0]).toStrictEqual({
    value: 3,
    name: 'First Attribute',
    isPercentage: true
  });
  expect(attributes[1]).toStrictEqual({
    value: 3,
    name: 'First Attribute',
    isPercentage: false
  });
});

test('equal with different count', () => {
  const lhs = [{
    value: 3,
    name: 'First Attribute',
    isPercentage: true,
  }, {
    value: 3,
    name: 'Second Attribute',
    isPercentage: true,
  }];
  const rhs = [{
    value: 3,
    name: 'First Attribute',
    isPercentage: true,
  }];
  const calculater = new EnchantedAttributeCalculater();
  expect(calculater.equal(lhs, rhs)).toBeTruthy();
});

test('not equal with different value', () => {
  const lhs = [{
    value: 3,
    name: 'First Attribute',
    isPercentage: true,
  }];
  const rhs = [{
    value: 4,
    name: 'First Attribute',
    isPercentage: true,
  }];
  const calculater = new EnchantedAttributeCalculater();
  expect(calculater.equal(lhs, rhs)).toBeFalsy();
});

test('not equal with different category', () => {
  const lhs = [{
    value: 3,
    name: 'First Attribute',
    isPercentage: true,
  }];
  const rhs = [{
    value: 3,
    name: 'First Attribute',
    isPercentage: false,
  }];
  const calculater = new EnchantedAttributeCalculater();
  expect(calculater.equal(lhs, rhs)).toBeFalsy();
});

test('better than with positive', () => {
  const lhs = [{
    value: 4,
    name: 'First Attribute',
    isPercentage: true,
  }];
  const rhs = [{
    value: 3,
    name: 'First Attribute',
    isPercentage: true,
  }];
  const calculater = new EnchantedAttributeCalculater();
  expect(calculater.betterThan(lhs, rhs)).toBeTruthy();
});

test('better than with negative', () => {
  const lhs = [{
    value: -4,
    name: 'First Attribute',
    isPercentage: true,
  }];
  const rhs = [{
    value: -3,
    name: 'First Attribute',
    isPercentage: true,
  }];
  const calculater = new EnchantedAttributeCalculater();
  expect(calculater.betterThan(lhs, rhs)).toBeTruthy();
});

test('better than with some equal attibutes', () => {
  const lhs = [{
    value: -3,
    name: 'First Attribute',
    isPercentage: true,
  }, {
    value: 6,
    name: 'Second Attribute',
    isPercentage: true,
  }];
  const rhs = [{
    value: -3,
    name: 'First Attribute',
    isPercentage: true,
  }, {
    value: 5,
    name: 'Second Attribute',
    isPercentage: true,
  }];
  const calculater = new EnchantedAttributeCalculater();
  expect(calculater.betterThan(lhs, rhs)).toBeTruthy();
});

test('better or equal than', () => {
  const calculater = new EnchantedAttributeCalculater();
  expect(calculater.betterOrEqualThan(
    [{ value: -3, name: 'First Attribute', isPercentage: true }],
    [{ value: -3, name: 'First Attribute', isPercentage: true }]
  )).toBeTruthy();
  expect(calculater.betterOrEqualThan(
    [{ value: -4, name: 'First Attribute', isPercentage: true }],
    [{ value: -3, name: 'First Attribute', isPercentage: true }]
  )).toBeTruthy();
  expect(calculater.betterOrEqualThan(
    [{ value: 4, name: 'First Attribute', isPercentage: true }],
    [{ value: 3, name: 'First Attribute', isPercentage: true }]
  )).toBeTruthy();
  expect(calculater.betterOrEqualThan(
    [{ value: -4, name: 'First Attribute', isPercentage: true }, 
     { value: 5, name: 'Second Attribute', isPercentage: true }],
    [{ value: -3, name: 'First Attribute', isPercentage: true },
     { value: 5, name: 'Second Attribute', isPercentage: true }]
  )).toBeTruthy();
  expect(calculater.betterOrEqualThan(
    [{ value: -4, name: 'First Attribute', isPercentage: true }, 
     { value: 5, name: 'Second Attribute', isPercentage: true }],
    [{ value: -3, name: 'First Attribute', isPercentage: true }]
  )).toBeTruthy();
  expect(calculater.betterOrEqualThan(
    [{ value: -4, name: 'First Attribute', isPercentage: true }, 
     { value: 5, name: 'Second Attribute', isPercentage: true }],
    [{ value: -5, name: 'First Attribute', isPercentage: true }]
  )).toBeFalsy();
  expect(calculater.betterOrEqualThan(
    [{ value: -4, name: 'First Attribute', isPercentage: true }, 
     { value: 5, name: 'Second Attribute', isPercentage: true }],
    [{ value: -4, name: 'First Attribute', isPercentage: true },
     { value: -5, name: 'Third Attribute', isPercentage: true }]
  )).toBeFalsy();
});

test('calculate single col probability', () => {
  const calculater = new EnchantedAttributeCalculater();
  const enchantableAttributes = [{
    probability: 0.5,
    name: 'First Attribute',
    isPercentage: true,
    start: 1,
    stop: 5,
    step: 1
  }, {
    probability: 0.5,
    name: 'Sencond Attribute',
    isPercentage: true,
    start: 1,
    stop: 5,
    step: 1
  }];
  const target = {
    value: 3,
    name: 'First Attribute',
    isPercentage: true,
  };
  expect(calculater.calculateSingleColProbability(enchantableAttributes, target)).toBe(0.3);
});

test('calculate single col probability out of range', () => {
  const calculater = new EnchantedAttributeCalculater();
  expect(calculater.calculateSingleColProbability([{
    probability: 0.5,
    name: 'First Attribute',
    isPercentage: true,
    start: 2,
    stop: 10,
    step: 2
  }], {
    value: 11,
    name: 'First Attribute',
    isPercentage: true,
  })).toBe(0);
  expect(calculater.calculateSingleColProbability([{
    probability: 0.5,
    name: 'First Attribute',
    isPercentage: true,
    start: -10,
    stop: -2,
    step: 2
  }], {
    value: -11,
    name: 'First Attribute',
    isPercentage: true,
  })).toBe(0);
});

test('calculate probability', () => {
  const calculater = new EnchantedAttributeCalculater();
  const rows = [{
    probability: 0.5,
    enchantableAttributes: [{
      probability: 0.5,
      name: 'First Attribute',
      isPercentage: true,
      start: 1,
      stop: 5,
      step: 1
    }, {
      probability: 0.5,
      name: 'Sencond Attribute',
      isPercentage: true,
      start: 1,
      stop: 5,
      step: 1
    }],
    rowNumber: 1
  }];
  const targets = [{
    value: 3,
    name: 'First Attribute',
    isPercentage: true,
  }];
  expect(calculater.calculateProbability(rows, targets)).toBe(0.15);
});

test('calculate probability with different order', () => {
  const calculater = new EnchantedAttributeCalculater();
  const rows = [{
    probability: 0.8,
    enchantableAttributes: [{
      probability: 0.5,
      name: 'First Attribute',
      isPercentage: true,
      start: 1,
      stop: 5,
      step: 1
    }, {
      probability: 0.5,
      name: 'Second Attribute',
      isPercentage: true,
      start: 1,
      stop: 5,
      step: 1
    }],
    rowNumber: 1
  }, {
    probability: 0.8,
    enchantableAttributes: [{
      probability: 0.5,
      name: 'First Attribute',
      isPercentage: true,
      start: 1,
      stop: 5,
      step: 1
    }],
    rowNumber: 2
  }];
  const targets = [{
    value: 3,
    name: 'Second Attribute',
    isPercentage: true,
  },{
    value: 3,
    name: 'First Attribute',
    isPercentage: true,
  }];
  expect(calculater.calculateProbability(rows, targets)).toBe(0.8 * 0.5 * 0.6 * 0.8* 0.5 * 0.6);
});

test('calculate probability with more than one posible enchantment', () => {
  const calculater = new EnchantedAttributeCalculater();
  const rows = [{
    probability: 0.8,
    enchantableAttributes: [{
      probability: 0.5,
      name: 'First Attribute',
      isPercentage: true,
      start: 1,
      stop: 5,
      step: 1
    }, {
      probability: 0.5,
      name: 'Second Attribute',
      isPercentage: true,
      start: 1,
      stop: 5,
      step: 1
    }],
    rowNumber: 1
  }, {
    probability: 0.8,
    enchantableAttributes: [{
      probability: 0.5,
      name: 'First Attribute',
      isPercentage: true,
      start: 1,
      stop: 5,
      step: 1
    }, {
      probability: 0.5,
      name: 'Second Attribute',
      isPercentage: true,
      start: 1,
      stop: 5,
      step: 1
    }],
    rowNumber: 2
  }];
  const targets = [{
    value: 3,
    name: 'Second Attribute',
    isPercentage: true,
  },{
    value: 3,
    name: 'First Attribute',
    isPercentage: true,
  }];
  expect(calculater.calculateProbability(rows, targets)).toBe(0.8 * 0.5 * 0.6 * 0.8* 0.5 * 0.6 * 2);
});