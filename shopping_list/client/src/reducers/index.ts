import { combineReducers } from "redux";
import shoppingListReducer from "./shoppingListReducer";
import { ShoppingListState } from "./shoppingListReducer";

export interface AppState {
  shoppingList: ShoppingListState;
}

export default combineReducers<AppState>({
  shoppingList: shoppingListReducer
});
