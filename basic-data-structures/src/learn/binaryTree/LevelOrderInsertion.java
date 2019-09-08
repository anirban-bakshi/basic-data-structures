package learn.binaryTree;

import java.util.LinkedList;
import java.util.Queue;

public class LevelOrderInsertion {

	static class Node {
		int data;
		Node left;
		Node right;
		
		public Node(int data) {
			this.data = data;
			this.left = this.right = null;
		}
	}
	
	static Node root;
	
	static void insert(Node temp, int data) {
		
		Queue<Node> queue = new LinkedList<>();
		queue.add(temp);
		
		while(!queue.isEmpty()) {
			temp = queue.peek();
			queue.remove();
			
			if(temp.left == null) {
				temp.left = new Node(data);
				break;
			} else {
				queue.add(temp.left);
			}
			
			if(temp.right == null) {
				temp.right = new Node(data);
				break;
			} else {
				queue.add(temp.right);
			}
		}
	}
	
	static void inorder(Node temp) {
		
		if(temp == null) {
			return;
		}
		
		inorder(temp.left);
		System.out.print(temp.data + " ");
		inorder(temp.right);
	}
	
	public static void main(String[] args) {
		root = new Node(10);
		insert(root, 11);
		insert(root, 7);
		insert(root, 9);
		insert(root, 15);
		insert(root, 8);
		insert(root, 12);
		
		/*
		 * tree created :		10
		 * 			     	  /    \
		 * 					 11     7
		 *                  /  \   / \
		 *                 9  15  8   12
		 */
		
		System.out.println("Inorder traversal : ");
		inorder(root);
		
	}

}
