class Solution:
    def minimumBuckets(self, street: str) -> int:
        return -1 if (street == 'H') else 0 if (street == '.') else -1 if ('HHH' in street) else -1 if ('HH' in street[:2:] or 'HH' in street[-2::]) else street.count('H') - street.count('H.H')