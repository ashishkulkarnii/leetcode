class TrieNode {
    private TrieNode[] links;
    private boolean is_end = false;
    
    public TrieNode() {
        links = new TrieNode[26];
    }
    
    public boolean hasKey(char c) {
        return links[c-'a'] != null;
    }
    
    public TrieNode get(char c) {
        return links[c-'a'];
    }
    
    public void put(char c, TrieNode node) {
        links[c-'a'] = node;
    }
    
    public void setEnd() {
        is_end = true;
    }
    
    public boolean isEnd() {
        return is_end;
    }
}


class Trie {
    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }
    
    public void insert(String word) {
        TrieNode node = root;
        for(int i = 0; i < word.length(); ++i) {
            char curr = word.charAt(i);
            if(!node.hasKey(curr))
                node.put(curr, new TrieNode());
            node = node.get(curr);
        }
        node.setEnd();
    }
    
    public boolean search(String word) {
        TrieNode node = root;
        for(int i = 0; i < word.length(); ++i) {
            char curr = word.charAt(i);
            if(!node.hasKey(curr))
                return false;
            node = node.get(curr);
        }
        return node.isEnd();
    }
    
    public boolean startsWith(String prefix) {
        TrieNode node = root;
        for(int i = 0; i < prefix.length(); ++i) {
            char curr = prefix.charAt(i);
            if(!node.hasKey(curr))
                return false;
            node = node.get(curr);
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */