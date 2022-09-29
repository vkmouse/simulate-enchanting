import React from "react";

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
          {stats.map(p => p.map(q => q))}
        </div>
      </div>
    );
  }
}

export default EnchantmentStatsView;