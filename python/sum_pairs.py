def sum_pairs(initial_List, desired_number):
    pairs = []

    for num1 in initial_List:
        for indexNum in range(1, len(initial_List), 1):
            print(indexNum)
            if num1 + initial_List[indexNum] == desired_number:
                pairs.append([num1,initial_List[indexNum]])
                initial_List[indexNum] = -1
    return pairs if len(pairs) != 0 else 'unable to find pairs'

print(sum_pairs([1,2,3,4,5, 7], 7))

# exports.sumPairs = function (intArr, desiredNumber) {
#     let pairs = []
#     for (let i = 0; i < intArr.length; i++) {
#         for (let j = i + 1; j < intArr.length; j++) {
#             if (intArr[i] + intArr[j] === desiredNumber) {
#                 pairs.push([intArr[i], intArr[j]])
#             }
#         }
#     }
#     return pairs.length === 0 ? 'unable to find pairs' : pairs
# }

