define("echarts/chart/funnel",["require","./base","zrender/shape/Text","zrender/shape/Line","zrender/shape/Polygon","../config","../util/ecData","../util/number","zrender/tool/util","zrender/tool/color","zrender/tool/area","../chart"],function(e){function t(e,t,i,a,o){n.call(this,e,t,i,a,o),this.refresh(a)}var n=e("./base"),i=e("zrender/shape/Text"),a=e("zrender/shape/Line"),o=e("zrender/shape/Polygon"),r=e("../config");r.funnel={zlevel:0,z:2,clickable:!0,legendHoverLink:!0,x:80,y:60,x2:80,y2:60,min:0,max:100,minSize:"0%",maxSize:"100%",sort:"descending",gap:0,funnelAlign:"center",itemStyle:{normal:{borderColor:"#fff",borderWidth:1,label:{show:!0,position:"outer"},labelLine:{show:!0,length:10,lineStyle:{width:1,type:"solid"}}},emphasis:{borderColor:"rgba(0,0,0,0)",borderWidth:1,label:{show:!0},labelLine:{show:!0}}}};var s=e("../util/ecData"),l=e("../util/number"),h=e("zrender/tool/util"),m=e("zrender/tool/color"),V=e("zrender/tool/area");return t.prototype={type:r.CHART_TYPE_FUNNEL,_buildShape:function(){var e=this.series,t=this.component.legend;this._paramsMap={},this._selected={},this.selectedMap={};for(var n,i=0,a=e.length;a>i;i++)if(e[i].type===r.CHART_TYPE_FUNNEL){if(e[i]=this.reformOption(e[i]),this.legendHoverLink=e[i].legendHoverLink||this.legendHoverLink,n=e[i].name||"",this.selectedMap[n]=t?t.isSelected(n):!0,!this.selectedMap[n])continue;this._buildSingleFunnel(i),this.buildMark(i)}this.addShapeList()},_buildSingleFunnel:function(e){var t=this.component.legend,n=this.series[e],i=this._mapData(e),a=this._getLocation(e);this._paramsMap[e]={location:a,data:i};for(var o,r=0,s=[],h=0,m=i.length;m>h;h++)o=i[h].name,this.selectedMap[o]=t?t.isSelected(o):!0,this.selectedMap[o]&&!isNaN(i[h].value)&&(s.push(i[h]),r++);if(0!==r){for(var V,U,d,p,c=this._buildFunnelCase(e),u=n.funnelAlign,g=n.gap,y=r>1?(a.height-(r-1)*g)/r:a.height,b=a.y,f="descending"===n.sort?this._getItemWidth(e,s[0].value):l.parsePercent(n.minSize,a.width),k="descending"===n.sort?1:0,x=a.centerX,_=[],h=0,m=s.length;m>h;h++)if(o=s[h].name,this.selectedMap[o]&&!isNaN(s[h].value)){switch(V=m-2>=h?this._getItemWidth(e,s[h+k].value):"descending"===n.sort?l.parsePercent(n.minSize,a.width):l.parsePercent(n.maxSize,a.width),u){case"left":U=a.x;break;case"right":U=a.x+a.width-f;break;default:U=x-f/2}d=this._buildItem(e,s[h]._index,t?t.getColor(o):this.zr.getColor(s[h]._index),U,b,f,V,y,u),b+=y+g,p=d.style.pointList,_.unshift([p[0][0]-10,p[0][1]]),_.push([p[1][0]+10,p[1][1]]),0===h&&(0===f?(p=_.pop(),"center"==u&&(_[0][0]+=10),"right"==u&&(_[0][0]=p[0]),_[0][1]-="center"==u?10:15,1==m&&(p=d.style.pointList)):(_[_.length-1][1]-=5,_[0][1]-=5)),f=V}c&&(_.unshift([p[3][0]-10,p[3][1]]),_.push([p[2][0]+10,p[2][1]]),0===f?(p=_.pop(),"center"==u&&(_[0][0]+=10),"right"==u&&(_[0][0]=p[0]),_[0][1]+="center"==u?10:15):(_[_.length-1][1]+=5,_[0][1]+=5),c.style.pointList=_)}},_buildFunnelCase:function(e){var t=this.series[e];if(this.deepQuery([t,this.option],"calculable")){var n=this._paramsMap[e].location,i=10,a={hoverable:!1,style:{pointListd:[[n.x-i,n.y-i],[n.x+n.width+i,n.y-i],[n.x+n.width+i,n.y+n.height+i],[n.x-i,n.y+n.height+i]],brushType:"stroke",lineWidth:1,strokeColor:t.calculableHolderColor||this.ecTheme.calculableHolderColor||r.calculableHolderColor}};return s.pack(a,t,e,void 0,-1),this.setCalculable(a),a=new o(a),this.shapeList.push(a),a}},_getLocation:function(e){var t=this.series[e],n=this.zr.getWidth(),i=this.zr.getHeight(),a=this.parsePercent(t.x,n),o=this.parsePercent(t.y,i),r=null==t.width?n-a-this.parsePercent(t.x2,n):this.parsePercent(t.width,n);return{x:a,y:o,width:r,height:null==t.height?i-o-this.parsePercent(t.y2,i):this.parsePercent(t.height,i),centerX:a+r/2}},_mapData:function(e){function t(e,t){return"-"===e.value?1:"-"===t.value?-1:t.value-e.value}function n(e,n){return-t(e,n)}for(var i=this.series[e],a=h.clone(i.data),o=0,r=a.length;r>o;o++)a[o]._index=o;return"none"!=i.sort&&a.sort("descending"===i.sort?t:n),a},_buildItem:function(e,t,n,i,a,o,r,l,h){var m=this.series,V=m[e],U=V.data[t],d=this.getPolygon(e,t,n,i,a,o,r,l,h);s.pack(d,m[e],e,m[e].data[t],t,m[e].data[t].name),this.shapeList.push(d);var p=this.getLabel(e,t,n,i,a,o,r,l,h);s.pack(p,m[e],e,m[e].data[t],t,m[e].data[t].name),this.shapeList.push(p),this._needLabel(V,U,!1)||(p.invisible=!0);var c=this.getLabelLine(e,t,n,i,a,o,r,l,h);this.shapeList.push(c),this._needLabelLine(V,U,!1)||(c.invisible=!0);var u=[],g=[];return this._needLabelLine(V,U,!0)&&(u.push(c.id),g.push(c.id)),this._needLabel(V,U,!0)&&(u.push(p.id),g.push(d.id)),d.hoverConnect=u,p.hoverConnect=g,d},_getItemWidth:function(e,t){var n=this.series[e],i=this._paramsMap[e].location,a=n.min,o=n.max,r=l.parsePercent(n.minSize,i.width),s=l.parsePercent(n.maxSize,i.width);return(t-a)*(s-r)/(o-a)+r},getPolygon:function(e,t,n,i,a,r,s,l,h){var V,U=this.series[e],d=U.data[t],p=[d,U],c=this.deepMerge(p,"itemStyle.normal")||{},u=this.deepMerge(p,"itemStyle.emphasis")||{},g=this.getItemStyleColor(c.color,e,t,d)||n,y=this.getItemStyleColor(u.color,e,t,d)||("string"==typeof g?m.lift(g,-.2):g);switch(h){case"left":V=i;break;case"right":V=i+(r-s);break;default:V=i+(r-s)/2}var b={zlevel:this.getZlevelBase(),z:this.getZBase(),clickable:this.deepQuery(p,"clickable"),style:{pointList:[[i,a],[i+r,a],[V+s,a+l],[V,a+l]],brushType:"both",color:g,lineWidth:c.borderWidth,strokeColor:c.borderColor},highlightStyle:{color:y,lineWidth:u.borderWidth,strokeColor:u.borderColor}};return this.deepQuery([d,U,this.option],"calculable")&&(this.setCalculable(b),b.draggable=!0),new o(b)},getLabel:function(e,t,n,a,o,r,s,l,U){var d,p=this.series[e],c=p.data[t],u=this._paramsMap[e].location,g=h.merge(h.clone(c.itemStyle)||{},p.itemStyle),y="normal",b=g[y].label,f=b.textStyle||{},k=g[y].labelLine.length,x=this.getLabelText(e,t,y),_=this.getFont(f),L=n;b.position=b.position||g.normal.label.position,"inner"===b.position||"inside"===b.position||"center"===b.position?(d=U,L=Math.max(r,s)/2>V.getTextWidth(x,_)?"#fff":m.reverse(n)):d="left"===b.position?"right":"left";var W={zlevel:this.getZlevelBase(),z:this.getZBase()+1,style:{x:this._getLabelPoint(b.position,a,u,r,s,k,U),y:o+l/2,color:f.color||L,text:x,textAlign:f.align||d,textBaseline:f.baseline||"middle",textFont:_}};return y="emphasis",b=g[y].label||b,f=b.textStyle||f,k=g[y].labelLine.length||k,b.position=b.position||g.normal.label.position,x=this.getLabelText(e,t,y),_=this.getFont(f),L=n,"inner"===b.position||"inside"===b.position||"center"===b.position?(d=U,L=Math.max(r,s)/2>V.getTextWidth(x,_)?"#fff":m.reverse(n)):d="left"===b.position?"right":"left",W.highlightStyle={x:this._getLabelPoint(b.position,a,u,r,s,k,U),color:f.color||L,text:x,textAlign:f.align||d,textFont:_,brushType:"fill"},new i(W)},getLabelText:function(e,t,n){var i=this.series,a=i[e],o=a.data[t],r=this.deepQuery([o,a],"itemStyle."+n+".label.formatter");return r?"function"==typeof r?r.call(this.myChart,{seriesIndex:e,seriesName:a.name||"",series:a,dataIndex:t,data:o,name:o.name,value:o.value}):"string"==typeof r?r=r.replace("{a}","{a0}").replace("{b}","{b0}").replace("{c}","{c0}").replace("{a0}",a.name).replace("{b0}",o.name).replace("{c0}",o.value):void 0:o.name},getLabelLine:function(e,t,n,i,o,r,s,l,m){var V=this.series[e],U=V.data[t],d=this._paramsMap[e].location,p=h.merge(h.clone(U.itemStyle)||{},V.itemStyle),c="normal",u=p[c].labelLine,g=p[c].labelLine.length,y=u.lineStyle||{},b=p[c].label;b.position=b.position||p.normal.label.position;var f={zlevel:this.getZlevelBase(),z:this.getZBase()+1,hoverable:!1,style:{xStart:this._getLabelLineStartPoint(i,d,r,s,m),yStart:o+l/2,xEnd:this._getLabelPoint(b.position,i,d,r,s,g,m),yEnd:o+l/2,strokeColor:y.color||n,lineType:y.type,lineWidth:y.width}};return c="emphasis",u=p[c].labelLine||u,g=p[c].labelLine.length||g,y=u.lineStyle||y,b=p[c].label||b,b.position=b.position,f.highlightStyle={xEnd:this._getLabelPoint(b.position,i,d,r,s,g,m),strokeColor:y.color||n,lineType:y.type,lineWidth:y.width},new a(f)},_getLabelPoint:function(e,t,n,i,a,o,r){switch(e="inner"===e||"inside"===e?"center":e){case"center":return"center"==r?t+i/2:"left"==r?t+10:t+i-10;case"left":return"auto"===o?n.x-10:"center"==r?n.centerX-Math.max(i,a)/2-o:"right"==r?t-(a>i?a-i:0)-o:n.x-o;default:return"auto"===o?n.x+n.width+10:"center"==r?n.centerX+Math.max(i,a)/2+o:"right"==r?n.x+n.width+o:t+Math.max(i,a)+o}},_getLabelLineStartPoint:function(e,t,n,i,a){return"center"==a?t.centerX:i>n?e+Math.min(n,i)/2:e+Math.max(n,i)/2},_needLabel:function(e,t,n){return this.deepQuery([t,e],"itemStyle."+(n?"emphasis":"normal")+".label.show")},_needLabelLine:function(e,t,n){return this.deepQuery([t,e],"itemStyle."+(n?"emphasis":"normal")+".labelLine.show")},refresh:function(e){e&&(this.option=e,this.series=e.series),this.backupShapeList(),this._buildShape()}},h.inherits(t,n),e("../chart").define("funnel",t),t});