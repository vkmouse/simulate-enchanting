import { action, autorun, makeObservable, observable } from "mobx";
import { EnchantableAttributeRow } from "../../Core/Core";
import DataSource from "../DataSource";
import EnchantmentSerialStore from "./EnchantmentSerialStore";

class EnchantableAttributeRowStore {
  @observable rows: EnchantableAttributeRow[] = [];
  protected enchantmentSerialStore: EnchantmentSerialStore;

  constructor(enchantmentSerialStore: EnchantmentSerialStore) {
    this.enchantmentSerialStore = enchantmentSerialStore;
    makeObservable(this);
  } 

  initialize() {
    autorun(() => this.update());
  }

  protected update() {
    if (this.enchantmentSerialStore.serialId !== '') {
      const dataSource = new DataSource();
      dataSource.getAttributesBySerialId(this.enchantmentSerialStore.serialId).then(
        rows => this.setRows(rows)
      );
    }
  }

  @action protected setRows(rows: EnchantableAttributeRow[]) {
    this.rows = rows;
  }
}

export class MockEnchantableAttributeRowStore extends EnchantableAttributeRowStore {
  protected update() {
    if (this.enchantmentSerialStore.serialId !== '') {
      if (this.enchantmentSerialStore.serialId === 1) {
        this.setRows([{
          enchantableAttributes: [],
          rowNumber: 1,
          probability: 1
        }]);
      } else {
        this.setRows([{
          enchantableAttributes: [],
          rowNumber: 1,
          probability: 1
        }, {
          enchantableAttributes: [],
          rowNumber: 2,
          probability: 1
        }]);
      }
    }
  }
}


export default EnchantableAttributeRowStore;