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
  
  equal(lhs: Array<EnchantedAttribute>, rhs: Array<EnchantedAttribute>): boolean {
    for (const attribute of rhs) {
      const found = lhs.find(p => this.compare(p, attribute));
      if (found === undefined || found.value !== attribute.value) {
        return false;
      }
    }
    return true;
  }

  betterThan(lhs: Array<EnchantedAttribute>, rhs: Array<EnchantedAttribute>): boolean {
    let isBetter = false;
    for (const attribute of rhs) {
      const found = lhs.find(p => this.compare(p, attribute));
      if (found === undefined || Math.abs(found.value) < Math.abs(attribute.value)) {
        return false;
      } else if (Math.abs(found.value) > Math.abs(attribute.value)) {
        isBetter = true;
      }
    }
    return isBetter;
  }

  betterOrEqualThan(lhs: Array<EnchantedAttribute>, rhs: Array<EnchantedAttribute>): boolean {
    return this.equal(lhs, rhs) || this.betterThan(lhs, rhs);
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