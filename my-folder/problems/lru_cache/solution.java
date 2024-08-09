class ListNode{
    int key;
    int val;
    ListNode prev;
    ListNode next;

    public ListNode(int key, int val){
        this.key=key;
        this.val=val;
    }
}
class LRUCache {
    int capacity;
    Map<Integer,ListNode> dic;
    ListNode head;
    ListNode tail;

    public LRUCache(int capacity) {
        this.capacity=capacity;
        dic=new HashMap<>();
        head=new ListNode(-1,-1);
        tail=new ListNode(-1,-1);
        head.next=tail;
        tail.prev=head;
    }

    public void add(ListNode node){
        ListNode temp = tail.prev;
        node.prev=temp;
        temp.next=node;
        tail.prev=node;
        node.next=tail;
    }

    public void remove(ListNode node){
        node.prev.next=node.next;
        node.next.prev=node.prev;
    }
    
    public int get(int key) {
        if (!dic.containsKey(key)) return -1;
        ListNode node = dic.get(key);
        remove(node);
        add(node);
        return node.val;
    }
    
    public void put(int key, int value) {
        if ( dic.containsKey(key)){
            ListNode node = dic.get(key);
            remove(node);
        }
        ListNode node = new ListNode(key, value);
        dic.put(key,node);
        add(node);
        if (dic.size()>capacity){
            ListNode toremove = head.next;
            remove(toremove);
            dic.remove(toremove.key);
        }
        
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */