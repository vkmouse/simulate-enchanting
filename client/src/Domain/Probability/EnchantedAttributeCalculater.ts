import { EnchantableAttribute, EnchantableAttributeRow, EnchantedAttribute, EnchantedAttributeRow, EnchantmentCategory } from "../../Core/Core";

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

  calculateProbability(rows: Array<EnchantableAttributeRow>, targets: Array<EnchantedAttribute>): number {
    if (targets.length === 0) {
      return 1;
    }
    if (rows.length === 0) {
      return 0;
    }
    let probability = 0;
    const target = targets[0];
    for (const row of rows) {
      const currProbability = this.calculateSingleColProbability(row.enchantableAttributes, target);
      const newRows = this.removeItemOnce(rows, row);
      const newTargets = this.removeItemOnce(targets, target);
      probability += row.probability * currProbability * this.calculateProbability(newRows, newTargets);
    }
    return probability;
  }

  calculateSingleColProbability(enchantableAttributes: Array<EnchantableAttribute>, target: EnchantedAttribute) {
    const found = enchantableAttributes.find(p => this.compare(p, target));
    if (found !== undefined) {
      const all: EnchantedAttribute[] = [];
      for (let i = found.start; i < found.stop + 1; i = i + found.step) {
        all.push({ ...found, value: i });
      }
      const betterOrEqual = all.filter(p => this.betterOrEqualThan([p], [target]));
      return found.probability * betterOrEqual.length / all.length;
    } else {
      return 0;
    }
  }

  private compare(lhs: EnchantmentCategory, rhs: EnchantmentCategory): boolean {
    return lhs.name === rhs.name && lhs.isPercentage === rhs.isPercentage;
  }

  private convertToAttribute(attributeRow: EnchantedAttributeRow): EnchantedAttribute {
    return {
      value: attributeRow.value,
      name: attributeRow.name,
      isPercentage: attributeRow.isPercentage
    };
  }

  private removeItemOnce<T>(arr: T[], value: T) {
    const newArr = [...arr];
    const index = newArr.indexOf(value);
    if (index > -1) {
      newArr.splice(index, 1);
    }
    return newArr;
  }
}

export default EnchantedAttributeCalculater;