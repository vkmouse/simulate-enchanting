import React from 'react';
import ComponentData from '../../Components/ComponentData';
import ToggleButton from '../../Components/CustomToggleButton';

interface IProps {
  rowData: ComponentData[]
  rowNumber: number
  rowProbability: number
  onRowNumberChange?: (value: NonNullable<unknown>) => void
}

class EnchantableAttributeInfoView extends React.Component<IProps> {
  render() {
    const { rowData, rowNumber, rowProbability, onRowNumberChange } = this.props;
    return (
      <div className='wrapper'>
        <div className='wrapper__title'>附魔屬性</div>
        <div className='wrapper__content'>
          <div className='wrapper__row'>
            <ToggleButton
              data={rowData}
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