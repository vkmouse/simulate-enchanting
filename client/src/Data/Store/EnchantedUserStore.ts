import { action, makeObservable, observable } from "mobx";
import { EnchantedAttribute, EnchantedUserProps, EnchantingTerminationCondition } from "../../Core/Core";

class EnchantedUserStore implements EnchantedUserProps {
  @observable condition: EnchantingTerminationCondition = EnchantingTerminationCondition.TimesReached;
  @observable times = 1;
  @observable targets: EnchantedAttribute[] = [];

  constructor() {
    makeObservable(this);
  }

  @action setCondition(value: EnchantingTerminationCondition) {
    this.condition = value;
  }
}

export default EnchantedUserStore;