import React from "react";
import { Button } from '@mui/material';

interface IProps {
  label?: string
  disabled?: boolean
  onClick?: () => void
}

function CustomButton(props: IProps) {
  const { label, disabled, onClick } = props;

  return (
    <Button 
      sx={{ backgroundColor: "#3B5998" }} 
      variant="contained" 
      onClick={onClick}
      disabled={disabled}
    >
      {label}
    </Button>
  );
}

export default CustomButton;