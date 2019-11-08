import React, { Component } from "react";
import {
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  Form,
  FormGroup,
  Label,
  Input
} from "reactstrap";
import { connect } from "react-redux";
import uuid from "uuid";
import { addItem } from "../actions/itemActions";
import { AppState } from "./../reducers/index";
import { ShoppingItem } from "../reducers/shoppingListReducer";

interface ItemModalOwnProps {}

interface ItemModalStateProps {}

interface ItemModalDispatchProps {
  addItem: (item: ShoppingItem) => void;
}

type ItemModalProps = ItemModalOwnProps &
  ItemModalStateProps &
  ItemModalDispatchProps;

interface ItemModalState {}

class itemModal extends Component<ItemModalProps, ItemModalState> {
  state = {
    modal: false,
    name: ""
  };

  toggle = () => {
    this.setState({
      modal: !this.state.modal
    });
  };

  // TODO: type event parameter
  onChange = (e: any) => {
    this.setState({ [e.target.name]: e.target.value });
  };

  onSubmit = (e: any) => {
    e.preventDefault();

    const newItem = {
      id: uuid(),
      name: this.state.name
    };

    // Add item via addItem action
    this.props.addItem(newItem);

    // Close modal
    this.toggle();
  };

  render() {
    return (
      <div>
        <Button
          color="dark"
          style={{ marginBottom: "2rem", marginTop: "2rem" }}
          onClick={this.toggle}
        >
          Add Item
        </Button>
        <Modal isOpen={this.state.modal} toggle={this.toggle}>
          <ModalHeader toggle={this.toggle}>Add To Shopping List</ModalHeader>
          <ModalBody>
            <Form onSubmit={this.onSubmit}>
              <FormGroup>
                <Label for="item">Item</Label>
                <Input
                  type="text"
                  name="name"
                  id="item"
                  placeholder="Add shopping item"
                  onChange={this.onChange}
                />
                <Button color="dark" style={{ marginTop: "2rem" }} block>
                  Add Item
                </Button>
              </FormGroup>
            </Form>
          </ModalBody>
        </Modal>
      </div>
    );
  }
}

const mapStateToProps = (state: AppState) => ({
  shoppingListItems: state.shoppingList.items
});

export default connect(
  mapStateToProps,
  { addItem }
)(itemModal);
