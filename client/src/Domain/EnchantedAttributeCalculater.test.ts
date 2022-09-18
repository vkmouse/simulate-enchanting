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
