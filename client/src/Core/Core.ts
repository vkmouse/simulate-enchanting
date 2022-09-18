export interface EnchantmentCategory {
  name: string
  isPercentage: boolean
}

export interface Enchanted {
  value: number
}

export interface EnchantedAttribute extends Enchanted, EnchantmentCategory {
}

export interface EnchantedAttributeRow extends Enchanted, EnchantmentCategory {
  rowNumber: number
}

export interface Enchantable {
  probability: number
}

export interface EnchantableAttribute extends Enchantable, EnchantmentCategory {
  start: number
  stop: number
  step: number
}

export interface EnchantableAttributeRow extends Enchantable {
  enchantableAttributes: Array<EnchantableAttribute>
  rowNumber: number
}

export enum EnchantingTerminationCondition {
  TimesReached,
  TargetReached
}

export interface EnchantedUserProps {
  condition: EnchantingTerminationCondition
  times?: number
  targets?: EnchantedAttribute[]
}