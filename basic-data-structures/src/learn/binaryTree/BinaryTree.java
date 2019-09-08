package learn.binaryTree;

public class BinaryTree {
	
	Node root;
	
	public BinaryTree(int data) {
		root = new Node(data);
	}
	
	public static void main(String[] args) {
		
		BinaryTree binaryTree = new BinaryTree(0);
		binaryTree.root.left = new Node(1);
		binaryTree.root.right = new Node(2);
		
	}

}

class Node {
	
	int data;
	Node left;
	Node right;
	
	public Node( int data ) {
		this.data = data;
		this.left = this.right = null;
	}
}
