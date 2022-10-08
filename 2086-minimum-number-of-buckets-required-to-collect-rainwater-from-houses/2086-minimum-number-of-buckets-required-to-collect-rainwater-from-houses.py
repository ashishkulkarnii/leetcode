class Solution:
    def minimumBuckets(self, street: str) -> int:
        return -1 if (street == 'H' or 'HHH' in street or 'HH' in street[:2:] or 'HH' in street[-2::]) else street.count('H') - street.count('H.H')