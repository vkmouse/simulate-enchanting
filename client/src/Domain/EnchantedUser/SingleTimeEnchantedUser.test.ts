import SingleTimeEnchantedUser from "./SingleTimeEnchantedUser";

test('enchant', () => {
  const singleTimeEnchantedUser = new SingleTimeEnchantedUser([{
    enchantableAttributes: [{
      name: 'First Attribute',
      isPercentage: true,
      start: 1,
      stop: 1,
      step: 1,
      probability: 1.0
    }, {
      name: 'Second Attribute',
      isPercentage: true,
      start: 1,
      stop: 3,
      step: 1,
      probability: 0.0
    }],
    rowNumber: 1,
    probability: 1.0
  }, {
    enchantableAttributes: [{
      name: 'Third Attribute',
      isPercentage: true,
      start: 0,
      stop: 0,
      step: 1,
      probability: 1.0
    }, {
      name: 'Fourth Attribute',
      isPercentage: true,
      start: 1,
      stop: 3,
      step: 1,
      probability: 0.0
    }],
    rowNumber: 2,
    probability: 1.0
  }]);

  expect(singleTimeEnchantedUser.enchant()).toStrictEqual([{
    isPercentage: true,
    name: "First Attribute",
    value: 1,
    rowNumber: 1
  }, {
    isPercentage: true,
    name: "Third Attribute",
    value: 0,
    rowNumber: 2
  }]);
});

test('enchant until', () => {
  const singleTimeEnchantedUser = new SingleTimeEnchantedUser([{
    enchantableAttributes: [{
      name: 'First Attribute',
      isPercentage: true,
      start: 1,
      stop: 2,
      step: 1,
      probability: 0.5
    }, {
      name: 'Second Attribute',
      isPercentage: true,
      start: 1,
      stop: 2,
      step: 1,
      probability: 0.5
    }],
    rowNumber: 1,
    probability: 1.0
  }, {
    enchantableAttributes: [{
      name: 'Third Attribute',
      isPercentage: true,
      start: 1,
      stop: 2,
      step: 1,
      probability: 0.5
    }, {
      name: 'Fourth Attribute',
      isPercentage: true,
      start: 1,
      stop: 2,
      step: 1,
      probability: 0.5
    }],
    rowNumber: 2,
    probability: 1.0
  }]);

  const conditions = [false, false, false, false, false, false, false, false];
  while (conditions.reduce((prev, curr) => prev && curr, true)) {
    const attributeRows = singleTimeEnchantedUser.enchant();
    if (attributeRows[0].name === 'First Attribute') {
      conditions[attributeRows[0].value] = true;
    } else {
      conditions[attributeRows[0].value + 2] = true;
    }
    if (attributeRows[1].name === 'Third Attribute') {
      conditions[attributeRows[1].value] = true;
    } else {
      conditions[attributeRows[1].value + 2] = true;
    }
  }
});
