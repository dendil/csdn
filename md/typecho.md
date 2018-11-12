<!DOCTYPE HTML>


--------------------

<?php $this->options->charset(); ?>		== UTF-8
<?php $this->options->title() ?>       	== dendy的博客

--------------------------------------------------------------------------------
<?php $this->archiveTitle(array(
            'category'  =>  _t('分类 %s 下的文章'),
            'search'    =>  _t('包含关键字 %s 的文章'),
            'tag'       =>  _t('标签 %s 下的文章'),
            'author'    =>  _t('%s 发布的文章')
        ), '', ' - '); ?>
        <?php $this->options->title(); ?>
        <?php if ($this->is('index')): ?> - 
        	<?php $this->options->description(); ?>
        <?php endif; ?>    == dendy的博客 - Just So So ...



<?php $this->options->themeUrl('style.css'); ?> ==https://caojie.top/usr/themes/Affinity/style.css

<?php $this->header(); ?>  ==
<meta name="description" content="Just So So ..." />
<meta name="keywords" content="typecho,php,blog" />
<meta name="generator" content="Typecho 1.1/17.10.30" />
<meta name="template" content="Affinity" />
<link rel="pingback" href="https://caojie.top/index.php/action/xmlrpc" />
<link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://caojie.top/index.php/action/xmlrpc?rsd" />
<link rel="wlwmanifest" type="application/wlwmanifest+xml" href="https://caojie.top/index.php/action/xmlrpc?wlw" />
<link rel="alternate" type="application/rss+xml" title="dendy的博客 &raquo; RSS 2.0" href="https://caojie.top/index.php/feed/" />
<link rel="alternate" type="application/rdf+xml" title="dendy的博客 &raquo; RSS 1.0" href="https://caojie.top/index.php/feed/rss/" />
<link rel="alternate" type="application/atom+xml" title="dendy的博客 &raquo; ATOM 1.0" href="https://caojie.top/index.php/feed/atom/" />
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------




<?php $this->options->siteUrl(); ?> ==  https://caojie.top/
<?php $this->options->title() ?> 第二行
<?php $this->options->themeUrl('affinity.png'); ?> == https://caojie.top/usr/themes/Affinity/affinity.png
<?php $this->options->description() ?> == Just So So ...

--------------------------------------------------------------------------------
  <li><a
  	<?php if($this->is('index')): ?> 
  		class="current"
  	<?php endif; ?> 
  	href="
  	<?php $this->options->siteUrl(); ?>
  	">
  	<?php _e('首页'); ?>
  </a></li>
  <?php $this->widget('Widget_Contents_Page_List')->to($pages); ?>
  <?php while($pages->next()): ?>
      <li><a
      	<?php if($this->is('page', $pages->slug)): ?>
      	 class="current"
      	<?php endif; ?> 
      	href="
      	<?php $pages->permalink(); ?> == https://caojie.top/index.php/sousuo.html
      	" title="
      	<?php $pages->title(); ?> == 搜索
      	">
      	<?php $pages->title(); ?> 同上
      </a></li>
  <?php endwhile; ?>

==
<li><a class="current" href="https://caojie.top/">首页</a></li>
<li><a href="https://caojie.top/index.php/sousuo.html" title="搜索">搜索</a></li>
<li><a href="https://caojie.top/index.php/22.html" title="列表">列表</a></li>

--------------------------------------------------------------------------------
--------------------------------------------------------------------------------



<?php $this->permalink() ?>  == https://caojie.top/index.php/archives/26/
<?php $this->title() ?> == JAVA &amp;&amp; JVM 的 工作原理，层次结构 以及 GC工作原理



--------------------------------------------------------------------------------


<?php if (array_key_exists('img',unserialize($this->___fields()))): ?>
	<?php $this->fields->img(); ?>
	<?php else: ?>
		<?php preg_match_all("/\<img.*?src\=(\'|\")(.*?)(\'|\")[^>]*>/i", $this->content, $matches);$imgCount = count($matches[0]);
if($imgCount >= 1){$img = $matches[2][0];
echo <<<Html
{$img}
Html;}
?>
<?php endif; ?>

 == http://img.caojie.top/java/jvm_2018100801.png   or 空

 --------------------------------------------------------------------------------
--------------------------------------------------------------------------------


<?php $this->excerpt(120, ' ...'); ?> == JVMJava 虚拟机（Java virtual machine，JVM）是运行 Java 程序必不可少的机制。JVM实现了Java语言最重要的特征：即平台无关性。这是因为：编译后的 Java 程序指令并不直接在硬件系统的 CPU  ...

<?php $this->date('Y-m-d'); ?> == 2018-10-13
<?php $this->date(); ?> == 2018-10-13 
<?php $this->category(', '); ?> == <a href="https://caojie.top/index.php/category/default/">所有</a> 
<?php $this->pageLink('<x aria-label="Previous" class="btn btn-primary">上一页</x>'); ?>
<?php $this->pageLink('<x aria-label="Next" class="btn btn-primary">下一页</x>','next'); ?>
<?php echo date('Y'); ?> == 2018
<?php $this->footer(); ?> 空