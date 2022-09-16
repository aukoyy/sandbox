/* 


*/

interface MultiSelectOption {
  label?: string;
  value: string | number;
}

const options = [{ value: "Apple" }, { value: "Banana" }, { value: "Peach" }];

const removeValue = (value: string | number) => {
  const updatedValues = options
    .filter((op: MultiSelectOption) => {
      return value !== op.value;
    })
    .reduce((acc, current) => {
      acc.push(current.value);
      return acc;
    }, []);

  // onChange(updatedValues);
};
