import { EnchantableAttributeRow, EnchantedAttributeRow } from "../../Core/Core";
import SingleRowEnchantedUser from "./SingleRowEnchantedUser";

class SingleTimeEnchantedUser {
  enchantableAttributeRows: EnchantableAttributeRow[];
  singleRowEnchantedUsers: SingleRowEnchantedUser[];

  constructor(enchantableAttributeRows: EnchantableAttributeRow[]) {
    this.enchantableAttributeRows = enchantableAttributeRows;
    this.singleRowEnchantedUsers = enchantableAttributeRows.map(p => new SingleRowEnchantedUser(p.enchantableAttributes));
  }

  enchant(): EnchantedAttributeRow[] {
    const enchantedAttributeRows: EnchantedAttributeRow[] = [];
    for (let i = 0; i < this.enchantableAttributeRows.length; i++) {
      const row = this.enchantableAttributeRows[i];
      const user = this.singleRowEnchantedUsers[i];
      if (Math.random() < row.probability) {
        const enchantedAttribute = user.enchant();
        enchantedAttributeRows.push({
            ...enchantedAttribute,
            rowNumber: row.rowNumber
        });
      }
    }
    return enchantedAttributeRows;
  }
}

export default SingleTimeEnchantedUser;