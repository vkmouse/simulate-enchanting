export interface Enchanted {
  value: number
}

export interface EnchantedAttribute extends Enchanted {
  name: string
  isPercentage: boolean
}

export interface EnchantedAttributeRow extends Enchanted {
  name: string
  isPercentage: boolean
  rowNumber: number
}

export interface Enchantable {
  probability: number
}

export interface EnchantableAttribute extends Enchantable {
  name: string
  isPercentage: boolean
  start: number
  stop: number
  step: number
}

export interface EnchantableAttributeRow extends Enchantable {
  enchantableAttributes: Array<EnchantableAttribute>
  rowNumber: number
}