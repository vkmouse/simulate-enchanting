import { EnchantableAttributeRow, EnchantedAttribute, EnchantedAttributeRow, EnchantedUserProps, EnchantingTerminationCondition } from "../../Core/Core";
import EnchantedAttributeCalculater from "../Probability/EnchantedAttributeCalculater";
import SingleTimeEnchantedUser from "./SingleTimeEnchantedUser";

class EnchantedUser {
  enchantableAttributeRows: EnchantableAttributeRow[];
  singleTimeEnchantedUser: SingleTimeEnchantedUser;

  constructor(enchantableAttributeRows: EnchantableAttributeRow[]) {
    this.enchantableAttributeRows = enchantableAttributeRows;
    this.singleTimeEnchantedUser = new SingleTimeEnchantedUser(enchantableAttributeRows);
  }

  enchant(props: EnchantedUserProps): EnchantedAttributeRow[][] {
    if (props.condition === EnchantingTerminationCondition.TimesReached &&
      props.times !== undefined) {
      return this.enchantUntilTimesReached(props.times);
    } else if (props.condition === EnchantingTerminationCondition.TargetReached &&
      props.targets !== undefined) {
      return this.enchantUntilTargetReached(props.targets);
    }
    return [];
  }

  enchantUntilTimesReached(times: number): EnchantedAttributeRow[][] {
    const results: EnchantedAttributeRow[][] = [];
    for (let i = 0; i < times; i++) {
      results.push(this.singleTimeEnchantedUser.enchant());
    }
    return results;
  }

  enchantUntilTargetReached(targetAttributes: EnchantedAttribute[]): EnchantedAttributeRow[][] {
    const results: EnchantedAttributeRow[][] = [];
    const calculater = new EnchantedAttributeCalculater();
    const last = () => results[results.length - 1];

    do {
      results.push(this.singleTimeEnchantedUser.enchant());
    } while (!calculater.betterOrEqualThan(last(), targetAttributes));
     
    return results;
  }
}

export default EnchantedUser;