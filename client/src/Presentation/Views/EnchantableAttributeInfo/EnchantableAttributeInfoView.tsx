import React from 'react';
import ToggleButton from '../../Components/CustomToggleButton';

interface IProps {
  rowQuantity: number
  rowNumber: number
  rowProbability: number
  onRowNumberChange?: (value: NonNullable<unknown>) => void
}

class EnchantableAttributeInfoView extends React.Component<IProps> {
  getToggleButtonData() {
    const { rowQuantity } = this.props;
    const array = [
      { name: '第一欄', value: 1 },
      { name: '第二欄', value: 2 },
      { name: '第三欄', value: 3 },
    ];
    return array.filter(p => rowQuantity >= p.value );
  }

  render() {
    const { rowNumber, rowProbability, onRowNumberChange } = this.props;
    return (
      <div className='wrapper'>
        <div className='wrapper__title'>附魔屬性</div>
        <div className='wrapper__content'>
          <div className='wrapper__row'>
            <ToggleButton
              data={this.getToggleButtonData()}
              value={rowNumber}
              toggleButtonProps={{ sx: { fontSize: 16, lineHeight: 1.2 } }}
              onChange={onRowNumberChange}
            />
            <div>
              <div>附魔欄位機率: {rowProbability}%</div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default EnchantableAttributeInfoView;