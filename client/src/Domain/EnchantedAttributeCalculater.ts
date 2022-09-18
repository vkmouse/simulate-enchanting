import { EnchantedAttribute, EnchantedAttributeRow } from "../Core/Core";

class EnchantedAttributeCalculater {
  sum(attributeRows: Array<EnchantedAttributeRow>): Array<EnchantedAttribute> {
    const attributes: Array<EnchantedAttribute> = [];

    for (const attributeRow of attributeRows) {
      const found = attributes.find(p => this.compare(p, attributeRow));
      if (found === undefined) {
        attributes.push(this.convertToAttribute(attributeRow));
      } else {
        found.value += attributeRow.value;
      }
    }

    return attributes;
  }

  private compare(lhs: EnchantedAttribute, rhs: EnchantedAttribute): boolean {
    return lhs.name === rhs.name && lhs.isPercentage === rhs.isPercentage;
  }

  private convertToAttribute(attributeRow: EnchantedAttributeRow): EnchantedAttribute {
    return {
      value: attributeRow.value,
      name: attributeRow.name,
      isPercentage: attributeRow.isPercentage
    };
  }
}

export default EnchantedAttributeCalculater;