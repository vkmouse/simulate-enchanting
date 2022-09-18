import SingleRowEnchantedUser from "./SingleRowEnchantedUser";

test('enchant', () => {
  const singleRowEnchantedUser = new SingleRowEnchantedUser([{
    name: 'First Attribute',
    isPercentage: true,
    start: 0,
    stop: 0,
    step: 1,
    probability: 0
  }, {
    name: 'Second Attribute',
    isPercentage: true,
    start: 0,
    stop: 0,
    step: 1,
    probability: 1
  }]);
  expect(singleRowEnchantedUser.enchant()).toStrictEqual({
    isPercentage: true,
    name: "Second Attribute",
    value: 0
  });
});

test('enchant until', () => {
  const singleRowEnchantedUser = new SingleRowEnchantedUser([{
    name: 'First Attribute',
    isPercentage: true,
    start: 1,
    stop: 3,
    step: 1,
    probability: 0.5
  }, {
    name: 'Second Attribute',
    isPercentage: true,
    start: 1,
    stop: 3,
    step: 1,
    probability: 0.5
  }]);

  const conditions = [false, false, false, false, false, false];
  while (conditions.reduce((prev, curr) => prev && curr, true)) {
    const attribute = singleRowEnchantedUser.enchant();
    if (attribute.name === 'First Attribute') {
      conditions[attribute.value] = true;
    } else {
      conditions[attribute.value + 3] = true;
    }
  }
});