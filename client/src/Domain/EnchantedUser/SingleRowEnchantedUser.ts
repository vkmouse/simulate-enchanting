import { EnchantableAttribute, EnchantedAttribute } from "../../Core/Core";
import ProbabilityConverter from "../Probability/ProbabilityConverter";
import RouletteSimulator from "../Probability/RouletteSimulator";

class SingleRowEnchantedUser {
  enchantableAttributes: EnchantableAttribute[];
  rouletteSimulator: RouletteSimulator;
  probabilities: number[];
  probabilityConverter: ProbabilityConverter;

  constructor(enchantableAttributes: EnchantableAttribute[]) {
    this.enchantableAttributes = enchantableAttributes;
    this.rouletteSimulator = new RouletteSimulator();
    this.probabilities = enchantableAttributes.map(p => p.probability);
    this.probabilityConverter = new ProbabilityConverter();
  }

  enchant(): EnchantedAttribute {
    const enchantableAttribute = this.selectEnchantableAttribute();
    const value = this.selectValue(enchantableAttribute);
    return {
      name: enchantableAttribute.name,
      isPercentage: enchantableAttribute.isPercentage,
      value: value
    };
  }

  private selectEnchantableAttribute(): EnchantableAttribute {
    const selected = this.rouletteSimulator.spin(this.probabilities);
    return this.enchantableAttributes[selected];
  }

  private selectValue(enchantableAttribute: EnchantableAttribute): number {
    const { start, stop, step } = enchantableAttribute;
    const values = this.probabilityConverter.expandRange(start, stop, step);
    const selected = this.rouletteSimulator.spin(Array(values.length).fill(1));
    return values[selected];
  }
}


export default SingleRowEnchantedUser;
