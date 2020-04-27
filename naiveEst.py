import math

BIN_WIDTH = 2
# numberArray form input data into a multi dimensional array
# e.g. for 1-dimensional: [1.1, 2.5, 3.4, 2.3]
# e.g. for 2-dimensional: [[1.1,2], [2.5,3], [3.4,2.3]]
# e.g. for 3-dimensional: [[1.1,1,2], [2.5,3,2]]
# e.g. for n-dimensional: [[1, 213, ..., n], [2, 323.2, 321.2 ..., n]]
dataArray = []


# 1-dimensional prediction
def naiveEstimatorForOneDimensional(input, numberArr):
    count = 0
    x1 = float(input - BIN_WIDTH / 2)
    x2 = float(input + BIN_WIDTH / 2)
    for x in numberArr:
        if x1 < x <= x2:
            count += 1
    return count / (metaDataRows * metaDataColumns * BIN_WIDTH)


# 2-dimensional prediction
def naiveEstimatorForTwoDimensional(inputPoint, pointArr):
    # bin volume = 2 ** 2 = 4
    binSize =  BIN_WIDTH ** metaDataColumns
    count = 0
    for i in range(len(pointArr)):
        pointDistance = math.sqrt(((inputPoint[0] - pointArr[i][0]) ** 2) + ((inputPoint[1] - pointArr[i][1]) ** 2))
        if pointDistance < 1:
            count += 1
    return count / (metaDataRows * binSize)


# 3-dimensional prediction
def naiveEstimatorForThreeDimensional(inputMatrix, matrixArr):
    # bin volume = 2 ** 3 = 8
    binVolume = BIN_WIDTH ** metaDataColumns
    count = 0
    for i in range(len(matrixArr)):
        matrixDistance = math.sqrt(((inputMatrix[0] - matrixArr[i][0]) ** 2) + ((inputMatrix[1] - matrixArr[i][1]) ** 2) + ((inputMatrix[2] - matrixArr[i][2]) ** 2))
        if matrixDistance < 1:
            count += 1
    return count / (metaDataRows * binVolume)


# n-dimensional prediction
# For simplicity, 2d and 3d prediction can be replaced by n-dimensional prediction method in general
def naiveEstimatorForNDimensional(inputMatrix, matrixArr):
    # bin volume = 2 ** N
    binVolume = BIN_WIDTH ** metaDataColumns
    count = 0
    for i in range(len(matrixArr)):
        matrixDistance = 0
        for j in range(len(matrixArr[i])):
            matrixDistance += (inputMatrix[j] - matrixArr[i][j]) ** 2
        matrixDistance = math.sqrt(matrixDistance)
        if matrixDistance < 1:
            count += 1
    return count / (metaDataRows * binVolume)


# main program
if __name__ == "__main__":
    inputFile = open("data.txt", "r")
    metaData = [x.strip() for x in inputFile.readline().split(',')]
    # number of data instances
    metaDataRows = int(metaData[0])
    # number of dimension, 1D, 2D, 3D or ..... nD
    metaDataColumns = int(metaData[1])

    for x in range(metaDataRows):
        data = [float(x) for x in inputFile.readline().split()]
        dataArray.append(data)
    inputFile.close()

    outputFile = open("output.txt", "w+")
    for x in range(metaDataRows):
        probability = 0
        # For simplicity, 2d and 3d prediction can be replaced by n-dimensional prediction method in general
        if metaDataColumns == 1:
            # 1 dimensional
            probability = naiveEstimatorForOneDimensional(dataArray[x], dataArray)
        elif metaDataColumns == 2:
            # 2 dimensional
            probability = naiveEstimatorForTwoDimensional(dataArray[x], dataArray)
        elif metaDataColumns == 3:
            # 3 dimensional
            probability = naiveEstimatorForThreeDimensional(dataArray[x], dataArray)
        else:
            # n dimensional
            probability = naiveEstimatorForNDimensional(dataArray[x], dataArray)
        outputFile.writelines(str(probability) + '\n')

    outputFile.close()

