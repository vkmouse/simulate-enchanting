import React from "react";
import { SxProps, ToggleButtonGroup, ToggleButton, Theme } from "@mui/material";
import ComponentData from "./ComponentData";

interface IProps {
  data: ComponentData[]
  value: NonNullable<unknown>
  toggleButtonProps?: { sx?: SxProps<Theme> }
  toggleButtonGroupProps?: { sx?: SxProps<Theme> }
  onChange?: (value: NonNullable<unknown>) => void
}

function CustomToggleButton(props: IProps) {
  const {
    data, 
    value, 
    toggleButtonProps, 
    toggleButtonGroupProps, 
    onChange
  } = props;

  const handleChange = (
    event: React.MouseEvent<HTMLElement>, 
    value: NonNullable<unknown> | null): void => {
    if (value !== null && onChange !== undefined) {
      onChange(value);
    }
  };

  return (
    <ToggleButtonGroup {...toggleButtonGroupProps}
      sx={{ minWidth: 195 }}
      color="primary" 
      exclusive 
      onChange={handleChange} 
      value={value}>
      {data.map(p => 
        <ToggleButton key={p.name} value={p.value} disabled={p.disabled} {...toggleButtonProps} size='small'>
          {p.name}
        </ToggleButton>
      )}
    </ToggleButtonGroup>
  );
}

export default CustomToggleButton;