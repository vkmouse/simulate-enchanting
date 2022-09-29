import React from "react";
import { TextField } from "@mui/material";

interface IProps {
  label: string
  value: number
  maxValue?: number
  onChange?: (value: number) => void
}

interface IState {
  focused: boolean
}

class NumberTextField extends React.Component<IProps, IState> {
  constructor(props: IProps) {
    super(props);
    this.state = {
      focused: false
    };
  }

  handleBlur = () => this.setState({ focused: false });
  handleFocus = () => this.setState({ focused: true });
  handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const onChange = this.props.onChange ?? (() => void 0);
    const maxValue = this.props.maxValue ?? Number.MAX_SAFE_INTEGER;
    const value = parseInt(event.target.value.replace(/\D/g, ''));
    onChange(Math.min(maxValue, value));
  };

  getValue() {
    if (this.state.focused) {
      return this.props.value;
    } else {
      return this.props.value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    }
  }

  render() {
    return (
      <TextField
        label={this.props.label}
        type="text"
        size='small'
        sx={{ marginLeft: 0.5, marginRight: 0.5, width: "31%" }}
        value={this.getValue()}
        onChange={this.handleChange}
        onBlur={this.handleBlur}
        onFocus={this.handleFocus}
        InputLabelProps={{
          shrink: true
        }}
      />
    );
  }
}

export default NumberTextField;