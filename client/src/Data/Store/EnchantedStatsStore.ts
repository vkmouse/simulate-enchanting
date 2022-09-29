import { action, makeObservable, observable } from "mobx";
import { EnchantedAttributeRow } from "../../Core/Core";

class EnchantedStatsStore {
  private maxRecording: number;
  @observable stats: EnchantedAttributeRow[][] = [];

  constructor(maxRecording: number) {
    this.maxRecording = maxRecording;
    makeObservable(this);
  }

  @action pushStats(value: EnchantedAttributeRow[][]) {
    this.stats = this.stats.concat(value);
    const removeQuantity = this.stats.length - this.maxRecording;
    if (removeQuantity > 0) {
      this.stats.splice(0, removeQuantity);
    }
  }

  @action clear() {
    this.stats = [];
  }
}

export default EnchantedStatsStore;