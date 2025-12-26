struct Node {
    Node* prev = nullptr;
    Node* next = nullptr;
    int key;
};

class LRUCache {
private:
    map<int, int> vals;
    map<int, Node*> freqs;
    int capacity;
    int count = 0;
    Node* oldest = nullptr;
    Node* newest = nullptr;

    void print(){
        // cout << format("count={} newest={} oldest={}", count, newest->key, oldest->key) << endl;

        // Node* head = newest;
        // int headCount = 0;
        // while (head){
        //     // cout << head->key << " -> ";
        //     head = head->next;
        //     headCount++;
        // }
        // // cout << endl;

        // Node* tail = oldest;
        // int tailCount = 0;
        // while (tail){
        //     // cout << tail->key << " <- ";
        //     tail = tail->prev;
        //     tailCount++;
        // }
        // // cout << endl;

        // if (headCount != tailCount){
        //     cout << "headCount != tailCount" << endl;
        // }
    }

    void refresh(int key){
        if (freqs[key] == newest){
            return;
        }

        // cout << format("Relink the list for {}", key) << endl;
        if (freqs[key]->prev){
            freqs[key]->prev->next = freqs[key]->next;
        }
        if (freqs[key]->next){
            freqs[key]->next->prev = freqs[key]->prev;
        }

        if (freqs[key] == oldest){
            oldest = oldest->prev;
        }

        freqs[key]->prev = nullptr;
        freqs[key]->next = newest;
        newest->prev = freqs[key];
        newest = freqs[key];

        // print();
    }

public:
    LRUCache(int capacity) {
        this->capacity = capacity;
    }
    
    int get(int key) {
        // cout << format("get({})", key) << endl;
        if (!vals.contains(key)){
            return -1;
        }

        this->refresh(key);
        return vals[key];
    }
    
    void put(int key, int value) {
        // cout << format("put({},{})", key, value) << endl;
        if (vals.contains(key)){
            // cout << format("Key {} exist, just need to update value", key) << endl;
            vals[key] = value;
            this->refresh(key);
            return;
        }

        if (count == capacity){
            // cout << format("Removing LRU {}", oldest->key) << endl;
            vals.erase(oldest->key);
            freqs.erase(oldest->key);

            Node* prev = oldest->prev;
            if (prev){
                prev->next = nullptr;
                delete oldest;
                oldest = prev;
            }
        }
        else {
            count++;
        }

        vals[key] = value;
        Node* a = new Node;
        a->key = key;
        a->next = newest;
        if (newest){
            newest->prev = a;
        }
        else {  // count == 0
            oldest = a;
        }
        newest = a;
        if (capacity == 1){
            oldest = a;
        }
        freqs[key] = a;
        // print();
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
