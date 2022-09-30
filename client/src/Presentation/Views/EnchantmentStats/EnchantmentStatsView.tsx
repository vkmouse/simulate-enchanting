import React from "react";
import Table from "../../Components/CustomTable";

interface IProps {
  stats: string[][]
}

class EnchantmentStatsView extends React.Component<IProps> {
  render() {
    const { stats } = this.props;
    return (
      <div className='wrapper'>
        <div className='wrapper__title'>附魔統計</div>
        <div className='wrapper__content'>
          <Table 
            columes={['第一欄', '第二欄', '第三欄']}
            rows={stats.map(p => [
              p.length > 0 ? p[0] : '',
              p.length > 1 ? p[1] : '',
              p.length > 2 ? p[2] : ''
            ])}
            rowsWidth={['33%', '33%', '33%']}
          />
        </div>
      </div>
    );
  }
}

export default EnchantmentStatsView;