<?php

//允许上传的图片后缀

$allowed_filetype = array('gif','jpeg','jpg','png');
//explode()是把字符串切分成数组;

$temp = explode('.',$_FILES['file']['name']);


echo '<br>';

//print_r($temp);

$extension = end($temp);//获取这个数组最后一个元素的值,即获取上传的这个文件的后缀名

if (
    (($_FILES['file']['type'] == 'image/gif')
        ||($_FILES['file']['type'] == 'image/jpeg')
        ||($_FILES['file']['type'] == 'image/jpg')
        ||($_FILES['file']['type'] == 'image/pjpeg')
        ||($_FILES['file']['type'] == 'image/x-png')
        || ($_FILES['file']['type'] == 'image/png'))

    &&($_FILES['file']['size']<204800) //上传文件的大小要小于200kb
    && in_array($extension,$allowed_filetype))
{

    if ($_FILES['file']['error']>0)
    {
        echo '错误::'.$_FILES['file']['error'].'<br>';
    }else
    {
        echo '上传文件名:'.$_FILES['file']['name'].'<br>';
        echo '文件类型:'.$_FILES['file']['type'].'<br>';

        echo '文件大小:'.$_FILES['file']['type'].'<br>';


        echo '文件临时存储的位置:'.$_FILES['file']['tmp_name'];
        echo '<br>';


        //判断当前目录下的upload目录是否存在该文件
        //如果没有upload目录,那就创建它;upload目录的权限为777

        if (file_exists('upload/'.$_FILES['file']['name']))
        {
            echo $_FILES['file']['name'].'文件已经存在';
        }
        else
        {
            //如果upload目录不存在该文件则将文件上传到upload目录下

            move_uploaded_file($_FILES['file']['tmp_name'],'upload/'.$_FILES['file']['name']);

            echo '文件存储在:'.'upload/'.$_FILES['file']['name'];

        }


    }

}
else
{

    echo '爽哥提示:这是非法的文件格式';


}