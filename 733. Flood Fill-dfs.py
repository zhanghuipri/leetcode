class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        rows = len(image)
        cols = len(image[0])

        if sr >= rows or sc >= cols:
            return
        
        orgcolor = image[sr][sc]
        if orgcolor == newColor: return image
        def dfs(i, j):
            if image[i][j] == orgcolor:
                print("%d %d 's rotten: %s" % (i,j, image))
                image[i][j]=newColor

                #开始递归
                if i-1 >= 0:#上
                    dfs(i-1, j)

                if j-1 >= 0:#左
                    dfs(i, j-1)

                if i+1 < rows:#下
                    dfs(i+1, j)

                if j+1 < cols:#右
                    dfs(i, j+1)
        
        dfs(sr, sc)
        return image
