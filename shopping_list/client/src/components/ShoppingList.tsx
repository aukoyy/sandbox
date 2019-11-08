import React, { Component } from "react";
import { Container, ListGroup, ListGroupItem, Button } from "reactstrap";
import { CSSTransition, TransitionGroup } from "react-transition-group";
import { connect } from "react-redux";
import { getItems, deleteItem } from "./../actions/itemActions";
import { AppState } from "./../reducers/index";
import { ShoppingItem } from "./../reducers/shoppingListReducer";

interface ShoppingListOwnProps {}

interface ShoppingListStateProps {
  shoppingListItems: ShoppingItem[];
}

interface ShoppingListDispatchProps {
  deleteItem: (id: string) => void;
  getItems: () => void;
}

type ShoppingListProps = ShoppingListOwnProps &
  ShoppingListStateProps &
  ShoppingListDispatchProps;

interface ShoppingListState {}

class ShoppingList extends Component<ShoppingListProps, ShoppingListState> {
  componentDidMount() {
    this.props.getItems();
  }

  onDeleteClick = (id: string) => {
    this.props.deleteItem(id);
  };

  render() {
    const { shoppingListItems } = this.props;
    return (
      <Container>
        <ListGroup>
          <TransitionGroup className="shopping-list">
            {shoppingListItems.map(({ id, name }) => (
              <CSSTransition key={id} timeout={500} classNames="fade">
                <ListGroupItem>
                  <Button
                    className="remove-btn"
                    color="danger"
                    size="sm"
                    onClick={this.onDeleteClick.bind(this, id)}
                  >
                    &times;
                  </Button>
                  {name}
                </ListGroupItem>
              </CSSTransition>
            ))}
          </TransitionGroup>
        </ListGroup>
      </Container>
    );
  }
}

const mapStateToProps = (state: AppState) => ({
  shoppingListItems: state.shoppingList.items
});

export default connect(
  mapStateToProps,
  { getItems, deleteItem }
)(ShoppingList);
