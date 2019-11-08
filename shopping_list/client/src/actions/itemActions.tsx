import { GET_ITEMS, DELETE_ITEM, ADD_ITEM } from "./types";
import { ShoppingItem } from "./../reducers/shoppingListReducer";

export const getItems = () => {
  return {
    type: GET_ITEMS
  };
};

export const deleteItem = (id: string) => {
  return {
    type: DELETE_ITEM,
    payload: id
  };
};

export const addItem = (item: ShoppingItem) => {
  return {
    type: ADD_ITEM,
    payload: item
  };
};
