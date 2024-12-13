class SortManager:
    def sort_items(self, items):
        sorted_items = sorted(items, 
                key=lambda x: 
                int(x[4].replace('(', '').replace(')', '')) if x[4].replace('(', '').replace(')', '').isdigit() else 0, 
                reverse=True)
        return sorted_items        
